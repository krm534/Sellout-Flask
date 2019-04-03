"""items table

Revision ID: bda98856ddd2
Revises: 6a05626bbcc7
Create Date: 2019-04-01 04:57:06.372775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bda98856ddd2'
down_revision = '6a05626bbcc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('vendorid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vendorid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('usertype', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'usertype')
    op.drop_table('item')
    # ### end Alembic commands ###
